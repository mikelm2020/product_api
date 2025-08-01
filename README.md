<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/mikelm2020/product_api">
    <img src="https://raw.githubusercontent.com/mikelm2020/product_api/main/assets/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">product_api</h3>

  <p align="center">
    Microservicio de productos
    <br />
    <a href="https://github.com/mikelm2020/product_api"><strong>Explorar la documentación »</strong></a>
    <br />
    <br />
    <a href="http://localhost:8000/">Ver Demo</a>
    ·
    <a href="https://github.com/mikelm2020/product_api/issues">Reportar Bug</a>
    ·
    <a href="https://github.com/mikelm2020/product_api/issues">Requerir Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Tabla de Contenidos</summary>
  <ol>
    <li>
      <a href="#about-the-project">Acerca del Proyecto</a>
      <ul>
        <li><a href="#built-with">Construido con</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Empezando</a>
      <ul>
        <li><a href="#prerequisites">Prerequisitos</a></li>
        <li><a href="#installation">Instalación</a></li>
      </ul>
    </li>
    <li><a href="#usage">Uso</a></li>
    <li><a href="#contact">Contacto</a></li>
    <li><a href="#acknowledgments">Agradecimientos</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## Acerca del Proyecto

![Product Name Screen Shot](https://raw.githubusercontent.com/mikelm2020/product_api/main/assets/api.png)



Los objetivos del proyecto son:
* Usar JWT con un modelo de usuario personalizado
* Login con username y contraseña
* Crear la REST API for operaciones CRUD  mediante Django Rest Framework
* Usar Swagger para documentar la REST API


<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Construido con



* [![Python][Python]][Python-url]
* [![Django][Django]][Django-url]
* [![DjangoREST][DjangoREST]][DjangoREST-url]
* [![Swagger][Swagger]][Swagger-url]
* [![JWT][JWT]][JWT-url]


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Empezando


### Prerequisitos

Este proyecto requiere que se instale docker y make




### Instalación


1. Clonar el repositorio
   ```sh
   git clone https://github.com/mikelm2020/product_api.git
   ```
2. Crear un entorno virtual de Python
```sh
   python -m venv .venv --prompt="product_api"
   ```
3. Ejecutar entorno
```sh
   source .venv activate
   ```
4. Preparar el entorno virtual
   ```sh
   pip install -r requirements.txt
   ```
5. Crear un archivo .env con sus valores para las variables de entono del archivo .env_example

6. Ejecutar los comandos (ya deben estar instalados los prerequisitos):
```sh
   make build
   make up
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Uso

Entrar al link de la demo en este archivo:
1. Crear un usuario en el endpoint post/api/users
2. Login con username y pasword en el edpoint post/login
3. Copar token
4. Clic en el  botón Authorize
5. Pegar token en el campo value
6. Clic en el botón Authorize
7. Clic en  el botón close
8. Can you use the API
9. Ejecutar los endpoints deseados

### Comandos importantes


Para crear las migraciones
```sh
   make makemigrations
```
Para aplicar las migraciones
```sh
   make migrate
```
Para iniciar el servidor
```sh
   make up
```
Para ejecutar las pruebas
```sh
   make test
```
Para ver la ayuda de los comandos del Makefile
```sh
   make help
```

  


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->

<!-- CONTACT -->
## Contacto

Miguel Angel López Monroy - [@miguellopezmdev](https://twitter.com/miguellopezmdev) - miguel.lopezm.dev@gmail.com

Project Link: [http://localhost:8000/](http://localhost:8000/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Agradecimientos

Mis recuros favoritos usados:

* [Choose an Open Source License](https://choosealicense.com)
* [Django Documentation](https://docs.djangoproject.com/es/5.2/)
* [Django Rest Framework Documentation](https://www.django-rest-framework.org/)
* [Django Class Based View Inspector](http://ccbv.co.uk/)
* [Classy Django Rest Framework](https://www.cdrf.co/)
* [Platzi Platform](https://platzi.com/)
* [Udemy Platform](https://www.udemy.com/)
* [Real Python Tutorials](https://realpython.com/)
* [Blog Developer.pe](http://www.developerpe.com/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/mikelm2020/product_api.svg?style=for-the-badge
[contributors-url]: https://github.com/mikelm2020/product_api/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/mikelm2020/product_api.svg?style=for-the-badge
[forks-url]: https://github.com/mikelm2020/product_api/network/members
[stars-shield]: https://img.shields.io/github/stars/mikelm2020/product_api.svg?style=for-the-badge
[stars-url]: https://github.com/mikelm2020/product_api/stargazers
[issues-shield]: https://img.shields.io/github/issues/mikelm2020/product_api.svg?style=for-the-badge
[issues-url]: https://github.com/mikelm2020/product_api/issues
[license-shield]: https://img.shields.io/github/license/mikelm2020/product_api.svg?style=for-the-badge
[license-url]: https://github.com/mikelm2020/product_api/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/miguellopezmdev
[product-screenshot]: https://github.com/mikelm2020/product_api/blob/82a8c694a418723faacf992c5dd76b6e328120f8/api_playlists.png
[Python]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Python-url]: https://www.python.org/
[Django]: https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white
[Django-url]: https://docs.djangoproject.com/es/5.2/topics/
[DjangoREST]: https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray
[DjangoREST-url]: https://www.django-rest-framework.org/
[Swagger]: https://img.shields.io/badge/-Swagger-%23Clojure?style=for-the-badge&logo=swagger&logoColor=white
[Swagger-url]: https://swagger.io/
[JWT]: https://img.shields.io/badge/JWT-black?style=for-the-badge&logo=JSON%20web%20tokens
[JWT-url]: https://jwt.io/