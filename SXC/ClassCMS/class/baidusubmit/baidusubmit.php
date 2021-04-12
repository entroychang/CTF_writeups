<?php
if(!defined('ClassCms')) {exit();}
class baidusubmit {
    function install() {
        if(!function_exists('curl_init')) {
            Return '未安装curl组件';
        }
        C($GLOBALS['C']['DbClass'].':createTable',__class__,array('title'=>'varchar(255)','url'=>'varchar(255)','cid'=>'int(11)','articleid'=>'int(11)','createtime'=>'bigint(10)','returninfo'=>'varchar(255)'));
    }
    function uninstall() {
        C($GLOBALS['C']['DbClass'].':delTable',__class__);
    }
    function config() {
        $configs=array();
        $configs[]=array('configname'=>'域名','hash'=>'sitedomain','inputhash'=>'text','defaultvalue'=>'','tips'=>'在<a href="https://ziyuan.baidu.com/site/index#/" style="color:#1E9FFF" target="_blank">百度搜索资源平台</a>中验证的站点域名,如classcms.com,不需要加http');
        $configs[]=array('configname'=>'TOKEN','hash'=>'sitetoken','inputhash'=>'text','defaultvalue'=>'','tips'=>'在<a href="https://ziyuan.baidu.com/site/index#/" style="color:#1E9FFF" target="_blank">百度搜索资源平台</a>中管理站点--普通收录中的准入密钥');
        $configs[]=array('configname'=>'HTTPS','hash'=>'https','inputhash'=>'switch','defaultvalue'=>'0','tips'=>'如果您的站点启用了https,并且需要推送https网址,则需要开启此项');
        Return $configs;
    }
    function auth() {
        Return array('show'=>'显示推送选项','history'=>'查看推送记录','clean'=>'清空记录');
    }
    function hook() {
        $hooks=array();
        $hooks[]=array('hookname'=>'show','hookedfunction'=>'admin:body','enabled'=>1);
        $hooks[]=array('hookname'=>'articleAdd','hookedfunction'=>'cms:article:add:=','enabled'=>1);
        Return $hooks;
    }
    function show() {
        if(!P('show')) {Return ;}
        if(isset($GLOBALS['C']['admin']['load']) && $GLOBALS['C']['admin']['load']=='admin:article:edit' && isset($_GET['cid']) && !isset($_GET['id']) && config('sitedomain') && config('sitetoken')) {
            if($channel=C('cms:channel:get',intval($_GET['cid']))) {
                if($articleroute=C('cms:route:get','article',$channel['modulehash'],$channel['classhash'])) {
                    echo('<script>layui.use([\'index\'],function(){layui.$(\'#columnitem .layui-tab-item\').eq(0).append(\'<div class="layui-form-item layui-form-item-width-100"><label class="layui-form-label">百度推送</label><div class="layui-input-right"><div class="layui-input-block"><input type="checkbox" name="_baidusubmit" lay-skin="switch"  lay-text="|"></div><div class="layui-form-mid">将此文章推送至百度</div></div></div>\');layui.form.render();});</script>');
                }
            }
        }
    }
    function articleAdd($class,$args=array(),$return=false) {
        if(isset($_POST['_baidusubmit']) && $return && isset($args[0]['cid'])) {
            $article=C('cms:article:getOne',array('cid'=>$args[0]['cid'],'where'=>array('id'=>$return)));
            C('this:submit',$article);
        }
    }
    function submit($article) {
        if(isset($article['link']) && substr($article['link'],0,1)=='/') {
            if(config('https')) {
                $url='https://';
            }else {
                $url='http://';
            }
            $domain=config('sitedomain');
            if(empty($domain)) {
                Return false;
            }
            $token=config('sitetoken');
            if(empty($token)) {
                Return false;
            }
            $url.=$domain.$article['link'];
            if(!isset($article['title'])) {$article['title']='未知';}
            if(!function_exists('curl_init')) {
                Return false;
            }
            $ch = curl_init();
            $options =  array(
                CURLOPT_URL => 'http://data.zz.baidu.com/urls?site='.$domain.'&token='.$token,
                CURLOPT_POST => true,
                CURLOPT_RETURNTRANSFER => true,
                CURLOPT_POSTFIELDS => $url,
                CURLOPT_HTTPHEADER => array('Content-Type: text/plain'),
            );
            curl_setopt_array($ch, $options);
            $result = curl_exec($ch);
            insert(array(
                'table'=>'baidusubmit',
                'title'=>$article['title'],
                'url'=>$url,
                'cid'=>$article['cid'],
                'articleid'=>$article['id'],
                'createtime'=>time(),
                'returninfo'=>$result
             ));
            Return true;
        }
        Return false;
    }
    function history() {
        $history_query=array();
        $history_query['table']='baidusubmit';
        $history_query['optimize']=true;
        $history_query['order']='id desc';
        $history_query['page']=page('pagesize',30);
        $array['historys']=all($history_query);
        V('template',$array);
    }
    function clean() {
        if(!isset($_POST['clean'])) {
            Return ;
        }
        $del_query=array();
        $del_query['table']='baidusubmit';
        if(del($del_query)) {
            Return C('admin:ajax','清空成功');
        }else {
            Return C('admin:ajax','清空失败',1);
        }
    }
}