<link rel="icon" type="image/x-ico" href="img/logo.ico">
<title>Equity: 热点追踪</title>
<style>
    body{
        margin: 0;
    }
</style>
<style type="text/css">@import url("css/down_menu.css");</style>
<style type="text/css">@import url("css/top_menu.css");</style>
<div class="equity_top_menu" style="height: 125px;">
    <img class="top_pic" src="img/main.jpg" alt="main_pic" style="height: auto;width: 100%;">
    <a class="top_a" href="server.php">服务器运行状态</a>
    <a class="top_a" href="data.php" style="margin-right: 100px;">数据库运行状态</a>
</div>
<div class="equity_down_menu">
    <a class="down_a" href="about.html" style="margin-left: -300px;">关于Equity</a>
    <a class="down_a" href="secret.html" style="margin-left: -200px;">隐私政策</a>
    <a class="down_a" href="rule.html" style="margin-left: -100px;">使用条款</a>
    <p class="down_p">©2021 Equity</p>
    <a class="down_a" href="source.html" style="margin-left: 130px;">量化原理</a>
    <a class="down_a" href="api.html" style="margin-left: 230px;">API接口</a>
</div>


<?php
function get_server_cpu_usage(){
 
 $load = sys_getloadavg(); 
 return $load [0]; 
 
} 
    echo '<div><h1 style="text-align: center;">服务器运行状态：正常</h1>
    <h2 style="text-align: center;">服务器承载量：'.get_server_cpu_usage().' %</h2>
    </div>';
?>