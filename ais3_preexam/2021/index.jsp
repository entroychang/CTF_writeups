<%--
  Created by IntelliJ IDEA.
  User: splitline
  Date: 2021/5/15
  Time: 3:02 上午
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>😈🐈</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bulma@0.9.2/css/bulma.min.css">
    <script defer src="https://use.fontawesome.com/releases/v5.15.1/js/all.js"></script>
    <style>
        html,
        body {
            font-family: 'Open Sans', sans-serif;
            background: #F0F2F4;
        }

        .hero-body {
            height: 400px;
        }

        .articles {
            margin: -150px 0 5rem;
        }
    </style>
</head>

<body>
<section class="hero is-black is-medium is-bold">
    <div class="hero-body">
        <div class="container has-text-centered">
            <h1 class="title">Cat Summoner</h1>
            <h2 class="subtitle">🐱🐱🐱</h2>
        </div>
    </div>
</section>


<div class="container">
    <section class="articles">
        <div class="column is-8 is-offset-2">
            <div class="card article">
                <div class="card-content">
                    <div class="media">
                        <div class="media-content has-text-centered">
                            <p class="title article-title">🐱召喚貓貓🐱</p>
                        </div>
                    </div>
                    <div class="content article-body">
                        <form action="summon.meow">
                            <div class="field">
                                <div class="control has-icons-left">
                                    <input class="input is-medium" type="text" name="name" placeholder="Name">
                                    <span class="icon is-small is-left">
                                            <i class="fa fa-user"></i>
                                    </span>
                                </div>
                            </div>
                            <div class="field">
                                <div class="control has-icons-left">
                                    <input class="input is-medium" type="text" name="num" placeholder="貓貓數量">
                                    <span class="icon is-small is-left">
                                            <i class="fas fa-cat"></i>
                                        </span>
                                </div>
                            </div>

                            <button class="button is-dark is-large is-fullwidth">
                                <span>召喚</span>
                            </button>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </section>
</div>
</body>

</html>
