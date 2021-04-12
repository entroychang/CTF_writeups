<?php if(!defined('ClassCms')) {exit();}?>
<!DOCTYPE html>
<html>
<head>{admin:head(百度推送)}</head>
<body>
  <div class="layui-fluid">
    <div class="layui-row">

<div class="layui-form">
    <div class="layui-card">
        <div class="layui-card-header">
            <div class="layui-row">
                <?php
                    $breadcrumb=array(
                        array('url'=>'?do=admin:class:config&hash=baidusubmit','title'=>'百度推送'),
                        array('title'=>'推送记录')
                    );
                ?>
                <div id="cms-breadcrumb">{admin:breadcrumb($breadcrumb)}</div>
                <div id="cms-right-top-button">
                {if P('clean')}<a class="layui-btn layui-btn-sm layui-btn-danger clean"><i class="layui-icon layui-icon-time"></i><b>清空日志</b></a>{/if}
                </div>
            </div>
        </div>
<div class="layui-card-body">

{if !config('sitedomain') || !config('sitetoken')}
    <blockquote class="layui-elem-quote layui-text">
        请先在<a href="?do=admin:class:setting&hash=baidusubmit">应用设置</a>中填写域名与TOKEN
    </blockquote>
{/if}

    <table class="layui-table" lay-skin="line" id="articles">
    <thead>
      <tr>
        <th>文章</th>
        <th>时间</th>
        <th>返回信息</th>
      </tr> 
    </thead>
    <tbody>
    {loop $historys as $history}
        <tr rel="{$history.id}">
            <td><a style="color:#1E9FFF" target="_blank" href="{$history.url}">{htmlspecialchars($history.title)}</a></td>
            <td>{date(m-d H:i:s,$history.createtime)}</td>
            <td>{htmlspecialchars($history.returninfo)}</td>
        </tr>
    {/loop}
    </tbody>
  </table>
    <div class="layui-row">
        <div id="cms-left-bottom-button" class="layui-btn-container"></div>
        <div id="cms-right-bottom-button" class="layui-btn-container">
            {admin:pagelist()}
        </div>
    </div>


</div>
    </div>

     </div>
  </div>
  </div>
  
<script>layui.use(['index'],function(){
    layui.$('.clean').click(function(){
        layui.layer.confirm('是否清空日志', {
          btn: ['清空','取消'],skin:'layer-danger',title:'请确认',shadeClose:1}, function(){
            layui.admin.req({type:'post',url:"?do=baidusubmit:clean",data:{'clean':1},async:true,beforeSend:function(){
                layui.admin.load('清空中...');
            },done: function(res){
                if (res.error==0)
                {
                    var confirm=layer.confirm(res.msg, {btn: ['好的','返回'],shadeClose:1},function(){layui.admin.events.reload();},function(){
                    layui.layer.close(confirm);
                    });
                }
            }});
        });
    });

});
</script>
{admin:body:~()}
</body>
</html>