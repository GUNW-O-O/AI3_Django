from django.http import HttpResponseForbidden
from django.shortcuts import redirect, render

from .decorators import user_is_post_owner
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from .models import Post

# Create your views here.

def index(request):
    return render(request, 'post/index.html')

@login_required  # 로그인한 사용자만 접근 가능
def create_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)  # DB 저장 전 객체 생성
            post.user = request.user        # 현재 로그인한 사용자 설정
            post.save()                     # DB에 저장
                            # 앱 : 패턴명
            return redirect('post:list')    # 게시글 목록으로 리다이렉트
        else:
            # 폼 유효성 검사 실패 시 에러 메시지 추가
            form.add_error(None, '게시글 작성에 실패했습니다. 다시 시도해주세요.')
    else:
        form = PostForm()
        
    return render(request, 'post/create.html', {'form':form})

def list_view(request):
    posts = Post.objects.all()
    
    return render(request, 'post/list.html', {'posts':posts})

def read_view(request, post_id):
    post = Post.objects.get(id=post_id) # 게시글 조회

    return render(request, 'post/read.html', {'post':post})

# 게시글 수정
@login_required  # 로그인한 사용자만 접근 가능
@user_is_post_owner # 소유자 검증
def update_view(request, post_id):
    post = Post.objects.get(id=post_id)     # 게시글 조회
    # 권한 체크
    # if post.user != request.user:
    #     return HttpResponseForbidden('수정 권한이 없습니다.')
    #     raise PermissionDenied
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)    # 기존 게시글 데이터로 폼 초기화
        if form.is_valid():
            form.save() # 수정된 게시글 저장
            return redirect('post:read', post_id=post.id)   # 수정 후 상세 페이지로 리다이렉트
    else:
        form = PostForm(instance=post)  # GET 요청 시 기존 데이터로 폼 초기화
    
    return render(request, 'post/update.html', {'form':form, 'post':post})

# 게시글 삭제
@login_required  # 로그인한 사용자만 접근 가능
@user_is_post_owner # 소유자 검증
def delete_view(request, post_id):
    post = Post.objects.get(id=post_id) # 게시글 조회
    if request.method == 'POST':
        post.delete()   # 게시글 삭제
        return redirect('post:list') # 삭제 후 목록 페이지로 리다이렉트
    
    # 게시글 삭제 실패
    return redirect('post:update', post_id=post.id)