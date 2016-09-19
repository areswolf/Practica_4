from django.contrib.auth.models import User
from django.http import HttpResponseNotFound
from django.views import View
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from blog.models import BlogPost, Category


class user_blog_list(View):

    def get(self, request, username):
        pk = User.objects.all().filter(username=username)
        categoryList = Category.objects.all()
        if pk is not None:
            possible_posts = BlogPost.objects.all().filter(owner=pk)
        else:
            return HttpResponseNotFound("El usuario no existe")

        if len(possible_posts) == 0:
            return HttpResponseNotFound("Este usuario no tiene ningún POST")
        else:
            posts_list = possible_posts
            # Paginador
            pag = paginador_3(request, posts_list, 10, 'postList')

            # context = {
            #     'post_list': pag['postList'],
            #     'totPost': posts_list,
            #     'paginator': pag,
            #     'user_info': pk
            # }

            context = {
                'category_list': categoryList,
                'post_list': pag['postList'],
                'totPost': posts_list,
                'paginator': pag,
                'user_info': pk,
                'username': username
            }
        return render(request, 'users/userBlogList.html', context)


class user_blog_list_filtered(View):
    def get(self, request, username, cathegory):
        categoryList = Category.objects.all()
        if cathegory == 'General':
            #direct = "{% url 'user_blog_list' username='" + username +"' %}"
            direct = "/blogs/" + username
            return redirect( direct )
        category = Category.objects.all().filter(category_name=cathegory)
        if category is not None:
            pk = User.objects.all().filter(username=username)
            if pk is not None:
                possible_posts = BlogPost.objects.all().order_by("-created_at").filter(owner=pk, blog_category=category)
            else:
                return HttpResponseNotFound("El usuario no existe")
        else:
            return HttpResponseNotFound("Este usuario no tiene ningún POST de esta categoría")

        if len(possible_posts) == 0:
            return HttpResponseNotFound("Este usuario no tiene ningún POST de esta categoría")
        else:
            posts_list = possible_posts
            # Paginador
            pag = paginador_3(request, posts_list, 10, 'postList')
            usuaio = username
            context = {
                'category_list': categoryList,
                'cathegory_posts': cathegory,
                'post_list': pag['postList'],
                'totPost': posts_list,
                'paginator': pag,
                'user_info': pk,
                'username': usuaio
            }
        return render(request, 'users/userBlogList.html', context)




class blog_list(View):
    """
    Renderiza el home con los últimos posts publicados y el listado de categorias
    :param request: objeto HttpRequest con los datos de la petición
    :return: HttpResponse con los datos de la respuesta
    """
    def get(self, request):
        blogs = User.objects.all()
        blogUser = []

        for i in range (0, blogs.count()):
            try:
                blogrest = BlogPost.objects.all().filter (owner=blogs[i].pk)[0]
            except:
                pass
            if blogrest is not None:
                blogUser.append(blogs[i])   # user
                blogUser.append(blogrest)   # Último post


        # Paginador
        pag = paginador_2(request, blogUser, 20, 'blogList')

        context = {
            'blog_list': pag['blogList'],
            'totPost': blogs,
            'paginator': pag,

        }

        return render(request, 'users/bloglist.html', context)


'''PARAMETROS:
request: Request de la vista
modelo: Modelo a utilizar en la paginación
paginas: Cantidad de paginas del paginador
nonRepPag: Identificador del result list
'''
def paginador(request, modelo, paginas, nonRegPag):
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


def paginador_2(request, modelo, paginas, nonRegPag):
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

def paginador_3(request, modelo, paginas, nonRegPag):
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
