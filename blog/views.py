from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View

from blog.forms import PostForm
from blog.models import BlogPost, Category


def home(request):
    """
    Renderiza el home con los últimos posts publicados y el listado de categorias
    :param request: objeto HttpRequest con los datos de la petición
    :return: HttpResponse con los datos de la respuesta
    """
    blog_post = BlogPost.objects.all().order_by("-created_at")
    categoryList = Category.objects.all()
    user_list = User.objects.all().select_related('owner')

    # Inicio el paginador
    pag = Paginador( request, blog_post, 9, 'blogs')

    context = {
        'category_list': categoryList,
        'post_list': pag['blogs'],
        'totPost': blog_post,
        'paginator': pag,
        'user_list': user_list
    }

    return render(request, 'blog/home.html', context)


class homeFiltered(View):
    def get(self, request, cathegory):
        if cathegory == 'General':
            return redirect('/')
        category = Category.objects.all().filter(category_name=cathegory)
        if category is not None:
            blog_post = BlogPost.objects.all().order_by("-created_at").filter(blog_category=category)
        else:
            return render(request, 'blog/home.html', {})
        user_list = User.objects.all().select_related('owner')
        categoryList = Category.objects.all()

        # Inicio el paginador
        pag = Paginador(request, blog_post, 9, 'blogs')

        context = {
            'category_list': categoryList,
            'post_list': pag['blogs'],
            'totPost': blog_post,
            'paginator': pag,
            'user_list': user_list
        }

        return render(request, 'blog/home.html', context)

class user_post_detail(View):

    def get(self, request, username, pk):
        pka = BlogPost.objects.all().filter(pk=pk)

        if len(pka) == 0:
            return HttpResponseNotFound("Este usuario no tiene ningún POST")
        else:
            posts_list = pka

            context = {
                'post_list': posts_list,
                'user_info': pk,
                'username': username
            }
        return render(request, 'blog/blogPostDetail.html', context)

class newPost (View):
    @method_decorator(login_required())
    def get(self, request):
        message = None
        post_form = PostForm()
        context = {'form': post_form, 'message': message}
        return render(request, 'blog/blog_creation.html', context)

    @method_decorator(login_required())
    def post(self, request):
        message = None
        post_with_user = BlogPost(owner=request.user)
        post_form = PostForm(request.POST, instance=post_with_user)
        if post_form.is_valid():
            new_post = post_form.save()
            post_form = PostForm ()
            message = 'Post creado satisfactoriamente.'

        context = {'form': post_form, 'message': message}
        return render(request, 'blog/blog_creation.html', context)



def Paginador(request, modelo, paginas, nonRegPag):
    # Retorna el objeto paginator para comenzar el trabajo
    result_list = Paginator(modelo, paginas)
    try:
        # Tomamos el valor de parametro page, usando GET
        page = int(request.GET.get('page'))
    except:
        page = 1

    # Si es menor o igual a 0 igualo en 1
    if page <= 0:
        page = 1

    # Si el parámetro es mayor a la cantidad
    # de paginas le igualo el parámetro con las cant de paginas
    if (page > result_list.num_pages):
        page = result_list.num_pages

    # Verificamos si esta dentro del rango
    if (result_list.num_pages >= page):
        # Obtengo el listado correspondiente al page
        pagina = result_list.page(page)
        Contexto = {nonRegPag: pagina.object_list,  # Asignamos registros de la pagina
                    'page': page,  # Pagina Actual
                    'pages': result_list.num_pages,  # Cantidad de Paginas
                    'has_next': pagina.has_next(),  # True si hay proxima pagina
                    'has_prev': pagina.has_previous(),  # true si hay Pagina anterior
                    'next_page': page + 1,  # Proxima pagina
                    'prev_page': page - 1,  # Pagina Anterior
                    'firstPage': 1,
                    }
        return Contexto

