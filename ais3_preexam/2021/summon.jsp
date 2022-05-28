<%@ page import="com.cat.Cat" %>
<%--
  Created by IntelliJ IDEA.
  User: splitline
  Date: 2021/5/15
  Time: 3:15 上午
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>

<html>
<head>
    <title>Summon Result</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bulma@0.9.2/css/bulma.min.css">
    <script defer src="https://use.fontawesome.com/releases/v5.15.1/js/all.js"></script>
    <style>
        .card {
            margin: 1em;
        }
    </style>
</head>
<body>
<section class="hero is-primary">
    <div class="hero-body">
        <p class="title">
            ${player.name}，您召喚了這些貓貓🐱。
        </p>
    </div>
</section>
<div class="container">
    <c:forEach items="${player.cats}" var="cat">
        <div class="card">
            <div class="card-content">
                <div class="content">
                    <p><strong>${cat.getName()}</strong></p>
                    <p>ATK: ${cat.getAttack()}</p>
                    <p>DFS: ${cat.getDefense()}</p>
                </div>
            </div>
        </div>
    </c:forEach>
    <c:if test="${loadFromToken == 0}">
        <a class="button is-primary" id="save" href="#">保存</a>
        （僅保存召喚等級）
    </c:if>
    <c:if test="${loadFromToken == 1}">
        <p>（貓咪🐱狀態已自 token 載入）</p>
    </c:if>
</div>

<script>
    const save = document.getElementById("save");
    const token = "${token}";
    save.onclick = function (event) {
        event.preventDefault();
        window.open("?token=" + encodeURIComponent(token), '_blank');
    }
</script>
</body>
</html>
