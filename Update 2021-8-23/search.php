<link rel="icon" type="image/x-ico" href="img/logo.ico">
<meta http-equiv="pragma" content="no-cache">
<meta http-equiv="Cache-Control" content="no-cache, must-revalidate">
<meta http-equiv="expires" content="0">
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
$search = $_GET['search'];
echo '<title>Equity: '.$search.'</title>';
if (empty($search)){
    echo '<div><h1 style="text-align: center;">搜索禁止为空</h1></div>';
}else if (!is_dir('equity/'.$search)){
    echo '<div><h1 style="text-align: center;">代码输入错误，请重试</h1>
    <h3 style="text-align: center;">3秒后跳转搜索界面</h3>
    </div>';
    header("refresh:5;url=index.html");
}else{
    echo '<div><h1 style="text-align: center;">'.$search.'</h1>
    <h3 style="text-align: center;">收盘趋势</h3>
    <img src="equity/'.$search.'/close.png" alt="pic_close" height="600px" width="auto" style="margin-left: 300px;">
    <h3 style="text-align: center;">开盘趋势</h3>
    <img src="equity/'.$search.'/TTM.png" alt="pic_close" height="600px" width="auto" style="margin-left: 300px;">
    <h3 style="text-align: center;">涨跌幅(%)</h3>
    <img src="equity/'.$search.'/turn.png" alt="pic_close" height="600px" width="auto" style="margin-left: 300px;">
    <h3 style="text-align: center;">成交趋势</h3>
    <img src="equity/'.$search.'/volume.png" alt="pic_close" height="600px" width="auto" style="margin-left: 300px;"></div>';
}
?>