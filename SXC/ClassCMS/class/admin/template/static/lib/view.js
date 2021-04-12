/**
 @Name：layuiAdmin 视图模块
 @Author：贤心
 @Site：http://www.layui.com/admin/
 @License：LPPL
 */

layui.define(["laytpl","layer"],function(A){var k=layui.jquery,t=layui.laytpl,x=layui.layer,p=layui.setter;layui.device();var z=layui.hint(),h=function(a){return new m(a)},m=function(a){this.id=a;this.container=k("#"+(a||"LAY_app_body"))};h.load=function(a){this.cmsload=x.msg(a,{icon:16,shade:.2,time:0})};h.loaded=function(){x.close(this.cmsload)};h.loading=function(a){h.removeLoad(a);a.append('<i class="view_loading"> </i><i class="layui-icon layui-icon-loading layui-icon layui-anim layui-anim-rotate layui-anim-loop view_loading"></i>')};
h.removeLoad=function(a){a.find("i.view_loading").remove()};h.req=function(a){var g=a.success,b=a.error,c=p.request,e=p.response,l=a.ifdebug,q=function(){return p.debug?"<br><cite>URL\uff1a</cite>"+a.url:""};a.data=a.data||{};a.headers=a.headers||{};if("undefined"!=typeof window.csrf){var n="string"===typeof a.data?JSON.parse(a.data):a.data;a.data.csrf=window.csrf}"undefined"==typeof l&&(l=1);"undefined"==typeof a.dataType&&(a.dataType="json");c.tokenName&&(n="string"===typeof a.data?JSON.parse(a.data):
a.data,a.data[c.tokenName]=c.tokenName in n?a.data[c.tokenName]:layui.data(p.tableName)[c.tokenName]||"",a.headers[c.tokenName]=c.tokenName in a.headers?a.headers[c.tokenName]:layui.data(p.tableName)[c.tokenName]||"");delete a.success;delete a.error;return k.ajax(k.extend({type:"get",dataType:"json",success:function(f){var d=e.statusCode;layui.admin.loaded();"json"!=a.dataType?"function"===typeof a.done&&a.done(f):("undefined"==typeof f[e.statusName]&&(f[e.statusName]=d.ok),"undefined"==typeof f[e.errorName]&&
(f[e.errorName]=0),0<f[e.errorName]&&("undefined"==typeof f[e.msgName]&&(f[e.msgName]="Error"),h.error(f[e.msgName])),f[e.statusName]==d.ok?"function"===typeof a.done&&a.done(f):f[e.statusName]==d.logout?(d=["<cite>Error\uff1a</cite> "+(f[e.msgName]||"\u60a8\u5df2\u9000\u51fa\u7cfb\u7edf,\u8bf7\u91cd\u65b0\u767b\u5165\u540e\u518d\u8bd5"),q()].join(""),h.error(d)):f[e.statusName]==d.csrf?(d=["<cite>Error\uff1a</cite> "+(f[e.msgName]||"\u975e\u6cd5\u63d0\u4ea4"),q()].join(""),h.error(d)):(d=["<cite>Error\uff1a</cite> "+
(f[e.msgName]||"\u8fd4\u56de\u72b6\u6001\u7801\u5f02\u5e38"),q()].join(""),h.error(d)));"function"===typeof g&&g(f)},error:function(f,d){layui.admin.loaded();l&&(f=["\u8bf7\u6c42\u5f02\u5e38\uff0c\u8bf7\u91cd\u8bd5<br><cite>\u9519\u8bef\u4fe1\u606f\uff1a</cite>"+d,q()].join(""),h.error(f));"function"===typeof b&&b()}},a))};h.popup=function(a){var g=a.success,b=a.skin;delete a.success;delete a.skin;return x.open(k.extend({type:1,title:"\u63d0\u793a",content:"",id:"LAY-system-view-popup",skin:"layui-layer-admin"+
(b?" "+b:""),shadeClose:!0,closeBtn:!1,success:function(c,e){var l=k('<i class="layui-icon" close>&#x1006;</i>');c.append(l);l.on("click",function(){x.close(e)});"function"===typeof g&&g.apply(this,arguments)}},a))};h.error=function(a,g){return h.popup(k.extend({content:a,maxWidth:300,area:"300px",offset:"66px",id:"LAY_adminError"},g))};m.prototype.render=function(a,g){var b=this;layui.router();a=p.views+a+p.engine;k("#LAY_app_body").children(".layadmin-loading").remove();h.loading(b.container);k.ajax({url:a,
type:"get",dataType:"html",data:{v:layui.cache.version},success:function(c){c="<div>"+c+"</div>";var e=k(c).find("title"),l={title:e.text()||(c.match(/<title>([\s\S]*)<\/title>/)||[])[1],body:c};e.remove();b.params=g||{};b.then&&(b.then(l),delete b.then);b.parse(c);h.removeLoad();b.done&&(b.done(l),delete b.done)},error:function(c){h.removeLoad();if(b.render.isError)return h.error("\u8bf7\u6c42\u89c6\u56fe\u6587\u4ef6\u5f02\u5e38\uff0c\u72b6\u6001\uff1a"+c.status);404===c.status?b.render("template/tips/404"):
b.render("template/tips/error");b.render.isError=!0}});return b};m.prototype.parse=function(a,g,b){var c="object"===typeof a,e=c?a:k(a),l=c?a:e.find("*[template]"),q=function(d){var y=t(d.dataElem.html()),u=k.extend({params:n.params},d.res);d.dataElem.after(y.render(u));"function"===typeof b&&b();try{d.done&&(new Function("d",d.done))(u)}catch(r){console.error(d.dataElem[0],"\n\u5b58\u5728\u9519\u8bef\u56de\u8c03\u811a\u672c\n\n",r)}},n=layui.router();e.find("title").remove();this.container[g?"after":
"html"](e.children());n.params=this.params||{};for(var f=l.length;0<f;f--)(function(){var d=l.eq(f-1),y=d.attr("lay-done")||d.attr("lay-then"),u=t(d.attr("lay-url")||"").render(n),r=t(d.attr("lay-data")||"").render(n),v=t(d.attr("lay-headers")||"").render(n);try{r=(new Function("return "+r+";"))()}catch(w){z.error("lay-data: "+w.message),r={}}try{v=(new Function("return "+v+";"))()}catch(w){z.error("lay-headers: "+w.message),v=v||{}}u?h.req({type:d.attr("lay-type")||"get",url:u,data:r,dataType:"json",
headers:v,success:function(w){q({dataElem:d,res:w,done:y})}}):q({dataElem:d,done:y})})();return this};m.prototype.autoRender=function(a,g){var b=this;k(a||"body").find("*[template]").each(function(c,e){c=k(this);b.container=c;b.parse(c,"refresh")})};m.prototype.send=function(a,g){a=t(a||this.container.html()).render(g||{});this.container.html(a);return this};m.prototype.refresh=function(a){var g=this,b=g.container.next().attr("lay-templateid");if(g.id!=b)return g;g.parse(g.container,"refresh",function(){g.container.siblings('[lay-templateid="'+
g.id+'"]:last').remove();"function"===typeof a&&a()});return g};m.prototype.then=function(a){this.then=a;return this};m.prototype.done=function(a){this.done=a;return this};A("view",h)});