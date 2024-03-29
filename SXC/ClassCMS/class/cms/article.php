<?php
if(!defined('ClassCms')) {exit();}
class cms_article {
    function getOne($config) {
        $config['pagesize']=1;
        $article=C('this:article:get',$config);
        if(isset($article[0])) {
            Return $article[0];
        }
        Return false;
    }
    function get($config) {
        if(!is_array($config)) {
            Return array();
        }
        if(!isset($config['classhash'])) {$config['classhash']=last_class();}
        if(!isset($config['all'])) {$config['all']=0;}elseif($config['all']==='1') {$config['all']=1;}
        if(!isset($config['enabled'])) {$config['enabled']=1;}
        if($config['all'] && !isset($config['cids'])) {
            if(isset($config['cid'])) {
                $config['cids']=C('this:article:allCid',$config['cid'],$config['classhash'],$config['all'],array(),$config['enabled']);
            }elseif(isset($GLOBALS['C']['channel']['id'])) {
                $config['cids']=C('this:article:allCid',$GLOBALS['C']['channel']['id'],$config['classhash'],$config['all'],array(),$config['enabled']);
            }
            if($config['all']===1) {
                if(count($config['cids'])==1) {unset($config['cids']);}
            }else {
                if(!count($config['cids'])) {unset($config['cids']);}
            }
        }
        if(isset($config['cids'])) {
            if(!is_array($config['cids'])) {
                $config['cids']=explode(';',$config['cids']);
            }
            if(!$cids_channel=C('this:channel:get',$config['cids'][0])) {
                Return array();
            }
            if($config['all']===1) {$channel=$cids_channel;}
            $config['modulehash']=$cids_channel['modulehash'];
        }
        if(isset($config['cid'])) {
            if(!C('this:common:verify',$config['cid'],'id') && $config['cid']!==0) {
                if(!$channel=C('this:channel:get',$config['cid'],$config['classhash'])) {
                    Return array();
                }
                $config['cid']=$channel['cid'];
            }
        }elseif(isset($config['modulehash'])) {
            if(!isset($config['cids'])) {
                if($config['enabled']) {
                    $module_channels=all(array('table'=>'channel','column'=>'id','where'=>array('enabled'=>1,'classhash'=>$config['classhash'],'modulehash'=>$config['modulehash'])));
                }else {
                    $module_channels=all(array('table'=>'channel','column'=>'id','where'=>array('classhash'=>$config['classhash'],'modulehash'=>$config['modulehash'])));
                }
                if(count($module_channels)>0 ) {
                    $config['cids']=array();
                    foreach($module_channels as $module_channel) {
                        $config['cids'][]=$module_channel['id'];
                    }
                }
            }
        }elseif(isset($GLOBALS['C']['channel']['id'])) {
            $config['cid']=$GLOBALS['C']['channel']['id'];
        }
        if(isset($config['cid'])) {
            if(!isset($channel) && !$channel=C('this:channel:get',$config['cid'])) {
                Return array();
            }
            $config['classhash']=$channel['classhash'];
            $config['modulehash']=$channel['modulehash'];
        }
        if(isset($config['modulehash'])) {
            if(!$module=C('this:module:get',$config['modulehash'],$config['classhash'])) {
                Return array();
            }
            if(!isset($config['table']) || empty($config['table'])) {
                $config['table']=$module['table'];
            }
        }
        if(!isset($config['table'])) {Return array();}
        if(isset($config['order'])) {
            $config['order']=$config['order'];
        }else {
            if(isset($channel['order'])) {
                $config['order']=$channel['order'];
            }elseif(isset($module['order'])) {
                $config['order']=$module['order'];
            }else {
                $config['order']='id desc';
            }
        }
        if($config['order']=='rand') {
            if($GLOBALS['C']['DbInfo']['kind']=='sqlitepdo') {
                $config['order']='random()';
            }else {
                $config['order']='rand()';
            }
        }
        if(!isset($config['pagesize'])) {
            if(isset($channel['pagesize']) && is_numeric($channel['pagesize'])) {
                $config['pagesize']=$channel['pagesize'];
            }elseif(isset($module['pagesize']) && is_numeric($module['pagesize'])) {
                $config['pagesize']=$module['pagesize'];
            }else {
                $config['pagesize']=10;
            }
        }
        if(!$config['pagesize']) {$config['pagesize']=99999999;}
        if(isset($config['column'])) {$config['column']='id,cid,uid'.$config['column'];}else {$config['column']='*';}
        if(!isset($config['start'])) {$config['start']=0;}
        if(!isset($config['sql'])) {$config['sql']='';}
        if(isset($config['cid'])) {
            if(empty($config['sql'])) {
                $config['sql'].='cid=\''.$config['cid'].'\'';
            }else {
                $config['sql'].=' and cid=\''.$config['cid'].'\'';
            }
        }
        if(isset($config['cids'])) {
            if(empty($config['sql'])) {
                $config['sql'].=where(array('cid'=>$config['cids']));
            }else {
                $config['sql'].=' and '.where(array('cid'=>$config['cids']));
            }
        }
        if(isset($config['where'])) {
            if(empty($config['sql'])) {
                $config['sql'].=where($config['where']);
            }else {
                $config['sql'].=' and '.where($config['where']);
            }
        }
        if(isset($config['page'])) {
            if(!C('this:common:verify',$config['page'],'id')) {
                if(empty($config['page'])) {
                    $config['pagename']='_page';
                }else {
                    $config['pagename']=$config['page'];
                }
                if(C('this:common:verify',@$_GET[$config['pagename']],'id')) {
                    $config['page']=$_GET[$config['pagename']];
                }else {
                    $config['page']=1;
                }
            }
            if(!isset($config['pagename'])) {
                $config['pagename']='_page';
            }
            if(!isset($config['articlecount'])) {
                $config['articlecount'] = total($config['table'],$config['sql']);
            }
            $config['start']=($config['page']-1)*$config['pagesize'];
            if($config['articlecount']%$config['pagesize']==0) {
                $config['pages']=$config['articlecount']/$config['pagesize'];
            }else {
                $config['pages']=intval($config['articlecount']/$config['pagesize'])+1;
            }
            if(!isset($config['pageurl'])) {
                if(!isset($config['pageroute']) || empty($config['pageroute'])) {
                    $config['pageroute']='list';
                }
                if(isset($channel)) {
                    $config['pageurl']=U($channel,$config['pageroute']);
                }else {
                    $config['pageurl']='';
                }
            }
            if(isset($channel) && !isset($config['channelurl'])) {
                $config['channelurl']=$channel['link'];
            }elseif(!isset($config['channelurl'])){
                $config['channelurl']='';
            }
            page('pagesize',$config['pagesize'],'page',$config['page'],'article',$config['articlecount'],'pagename',$config['pagename'],'url',$config['pageurl'],'channelurl',$config['channelurl']);
        }
        $GLOBALS['C']['article_query']=$config;
        if(!isset($config['route']) || empty($config['route'])) {$config['route']='article';}
        $article_query=array();
        $article_query['table']=$config['table'];
        $article_query['where']=$config['sql'];
        $article_query['column']=$config['column'];
        $article_query['offset']=$config['start'];
        $article_query['limit']=$config['pagesize'];
        $article_query['order']=$config['order'];
        $article_query['optimize']=true;
        $articles=all($article_query);
        foreach($articles as $key=>$article) {
            if(isset($channel)) {
                if($channel['id']==$article['cid']) {
                    $this_channel=$channel;
                }else {
                    $this_channel=C('this:channel:get',$article['cid']);
                }
            }else {
                if(isset($GLOBALS['channel'][$article['cid']])) {
                    $this_channel=$GLOBALS['channel'][$article['cid']];
                }else {
                    $this_channel=C('this:channel:get',$article['cid']);
                    $GLOBALS['channel'][$article['cid']]=$this_channel;
                }
            }
            if(!isset($articles[$key]['link']) || empty($articles[$key]['link'])) {
                $articles[$key]['link']=U($this_channel,$config['route'],$article);
            }
            if(!isset($articles[$key]['key'])) {
                $articles[$key]['key']=$key;
            }
            if(isset($config['rowstyle']) && !isset($article['rowstyle'])) {
                foreach($config['rowstyle'] as $rowstyle_key=>$rowstyle_val) {if($rowstyle_key==$key) {$articles[$key]['rowstyle']=$rowstyle_val;}}
                if(!isset($articles[$key]['rowstyle'])) {$articles[$key]['rowstyle']='';}
            }
            if(isset($config['stepstyle'])) {
                foreach($config['stepstyle'] as $stepstyle_key=>$stepstyle_val) {if(($key+1)%$stepstyle_key==0) {$articles[$key]['stepstyle']=$stepstyle_val;}}
                if(!isset($articles[$key]['stepstyle'])) {$articles[$key]['stepstyle']='';}
            }
        }
        Return $articles;
    }
    function add($config) {
        if(!isset($config['cid'])) {
            Return false;
        }
        if(!$channel=C('this:channel:get',$config['cid'])) {
            Return false;
        }
        if(!$module=C('this:module:get',$channel['modulehash'],$channel['classhash'])) {
            Return false;
        }
        $columns=C('this:form:all','column',$module['hash'],$module['classhash']);
        $columns=C('this:form:getColumnCreated',$columns,$module['table']);
        foreach($columns as $column) {
            if(!isset($config[$column['hash']])) {
                $column=C('this:form:build',$column['id']);
                $config[$column['hash']]=C('this:input:defaultvalue',$column);
            }
        }
        if(!isset($config['table'])) {
            $config['table']=$module['table'];
        }
        Return insert($config);
    }
    function edit($config) {
        if(!isset($config['cid']) || !isset($config['id'])) {
            Return false;
        }
        if(!$channel=C('this:channel:get',$config['cid'])) {
            Return false;
        }
        if(!$module=C('this:module:get',$channel['modulehash'],$channel['classhash'])) {
            Return false;
        }
        if(!isset($config['table'])) {
            $config['table']=$module['table'];
        }
        $config['where']=array('id'=>$config['id']);
        unset($config['id']);
        Return update($config);
    }
    function del($config) {
        if(!isset($config['cid'])) {
            Return false;
        }
        if(!$channel=C('this:channel:get',$config['cid'])) {
            Return false;
        }
        if(!$module=C('this:module:get',$channel['modulehash'],$channel['classhash'])) {
            Return false;
        }
        if(!isset($config['table'])) {
            $config['table']=$module['table'];
        }
        if(isset($config['id'])) {
            $config['where']=array('id'=>$config['id']);
        }
        if(!isset($config['where'])) {
            Return false;
        }
        unset($config['id']);
        Return del($config);
    }
    function allCid($cid,$classhash='',$all=1,$cids=array(),$enabled=1) {
        if(empty($classhash)) {$classhash=last_class();}
        if($all) {
            if(!$channel=C('this:channel:get',$cid,$classhash)) {
                Return array();
            }
            $cid=$channel['id'];
            if($all===1) {
                $cids[]=$cid;
            }
        }
        $sonchannels=C('this:channel:all',$cid,$classhash,99999999,false,$enabled);
        if(count($sonchannels)) {
            foreach($sonchannels as $sonchannel) {
                $cids[]=$sonchannel['id'];
                $cids=C('this:article:allCid',$sonchannel['id'],$classhash,0,$cids,$enabled);
            }
        }
        Return $cids;
    }
    function getVar($channel,$varhash) {
        if(!is_array($channel)) {
            if(!$channel=C('this:channel:get',$channel)) {
                Return false;
            }
        }
        $var_value=C('this:config:get',C('this:article:varStr',$channel,$varhash),$channel['classhash']);
        if($var_value===false) {
            if($var=C('this:form:get',$varhash,'var',$channel['modulehash'],$channel['classhash'])) {
                $var_value=$var['defaultvalue'];
            }
        }
        Return $var_value;
    }
    function getVars($channel,$vars) {
        if(!is_array($channel)) {
            if(!$channel=C('this:channel:get',$channel)) {
                Return false;
            }
        }
        $hashs=array();
        foreach($vars as $key=>$thisvar) {
            $hashs[]=C('this:article:varStr',$channel,$thisvar['hash']);
        }
        $values=C('this:config:gets',$hashs,$channel['classhash']);
        foreach($vars as $key=>$thisvar) {
            if($values[$key]===false) {
                $values[$key]=$thisvar['defaultvalue'];
            }
            $vars[$key]['value']=$values[$key];
        }
        Return $vars;
    }
    function setVar($channel,$varhash,$value='') {
        if(!is_array($channel)) {
            if(!$channel=C('this:channel:get',$channel)) {
                Return false;
            }
        }
        unset($GLOBALS['channel'][$channel['id']]);
        Return C('this:config:set',C('this:article:varStr',$channel,$varhash),$value,0,$channel['classhash']);
    }
    function delVar($channel,$varhash) {
        if(!is_array($channel)) {
            if(!$channel=C('this:channel:get',$channel)) {
                Return false;
            }
        }
        unset($GLOBALS['channel'][$channel['id']]);
        Return C('this:config:del',C('this:article:varStr',$channel,$varhash),$channel['classhash']);
    }
    function varStr($channel,$varhash) {
        Return $channel['classhash'].':'.$channel['id'].':article:var:'.$varhash;
    }
}