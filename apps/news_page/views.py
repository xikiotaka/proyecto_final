from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views import View
from .models import Post, Categoria, Like, Comentario
from .forms import ComentarioForm
from django.shortcuts import render


###Vista para meter dentro de una lista las publicaciones existentes
def post_list(request):
    posts = Post.objects.filter(activo=True).order_by('-publicado')
    return render(request, 'app/post_list.html', {'posts': posts})

###Vista para ver a detalle las características de una publicación "x", hay que ver los errores si no se pone ningún dato
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comentarios = post.comentario.all()  ###Obtener todos los comentarios relacionados a "x"

    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.save()  ###Para poder guardar el comentario en la base de datos
            post.comentario.add(comentario)  ###Agregar el comentario al post
            return redirect('post_detail', post_id=post.id)  ###Para poder redirigir a la vista del post

    else:
        form = ComentarioForm()

    return render(request, 'post_detail.html', {'post': post, 'form': form, 'comentarios': comentarios})

###Vista para poder realizar una nueva publicación de "cero"
class PostCreateView(View): ###Se crea una clase para poder manejar las acciones de forma separada pero dentro de un mismo elemento, se pueden agregar las funciones que se quisieran...
    def get(self, request):###pudiendo agregarse de forma flexible y progresiva funciones como eliminar u otras.
        return render(request, 'app/post_create.html') ###Nota, ver el HTML de qué panera se puede

    def post(self, request):
        titulo = request.POST['titulo']
        subtitulo = request.POST['subtitulo']
        texto = request.POST['texto']
        categoria_id = request.POST.get('categoria')
        imagen = request.FILES.get('imagen')

        post = Post.objects.create(
            titulo=titulo,
            subtitulo=subtitulo,
            texto=texto,
            categoria_id=categoria_id,
            imagen=imagen
        )
        return redirect('post_detail', post_id=post.id)

###Vista para agregar un "me gusta" a una publicación "x"
def add_like(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    Like.objects.create(post=post)
    return redirect('post_detail', post_id=post.id)

###Vista para crear una lista de categorías
def categoria_list(request):
    categorias = Categoria.objects.all()
    return render(request, 'app/categoria_list.html', {'categorias': categorias})

###HttpResponse con un mensaje genérico, ésto lo vimos en clase para poder corroborar si existen errores y el manejo de los mismos sin necesidad  de usar un template de HTML
def example_response(request):
    return HttpResponse("Este es un mensaje simple usando HttpResponse.")

def news_page(request):
    return render(request, 'news_page.html')