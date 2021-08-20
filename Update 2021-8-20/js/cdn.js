var time = 0
function timeset(){
    time = time + 1
    if (time==5){
        var browser = getExploreName();
        if (browser=="Unkonwn"){
            document.getElementById('cdn').innerHTML='Your browser is not a legal browser.';
            document.getElementById('cdn2').innerHTML='Your IP address has been locked for 60 seconds.';
            var date = new Date(); 
            date.setTime(date.getTime() + (60 * 1000)); 
            $.cookie('lock', 'true',{expires: date});
            window.setTimeout('window.location.href="502.html";',3000);
        }
        else{
            window.location.href="things.html";
        }
    }
    if (time==2){
        if (getExploreName()=="Unkonwn"){
        document.getElementById('cdn1').innerHTML='Your browser is '+getExploreName()+',The server refused to redirect...';}
        else{document.getElementById('cdn1').innerHTML='Your browser is '+getExploreName()+',Redirecting...';}
    }
}
window.setInterval('timeset();',1000);
var t = 0;
function setht(){
    t = t+1;
    if (t == 3){t=0}
    if (t==0){document.getElementById('cdn').innerHTML='Waiting to check your browser.';}
    else if (t==1){document.getElementById('cdn').innerHTML='Waiting to check your browser..';}
    else{document.getElementById('cdn').innerHTML='Waiting to check your browser...';}
}
window.setInterval('setht();',500);
function getExploreName(){
    var userAgent = navigator.userAgent;
    if(userAgent.indexOf("Opera") > -1 || userAgent.indexOf("OPR") > -1){
      return 'Opera';
    }
    else if(userAgent.indexOf("compatible") > -1 && userAgent.indexOf("MSIE") > -1){
      return 'IE';
    }
    else if(userAgent.indexOf("Edge") > -1){
       return 'Edge';
    }
    else if(userAgent.indexOf("Firefox") > -1){
       return 'Firefox';
    }
    else if(userAgent.indexOf("Safari") > -1 && userAgent.indexOf("Chrome") == -1){
      return 'Safari';
    }
    else if(userAgent.indexOf("Chrome") > -1 && userAgent.indexOf("Safari") > -1){
       return 'Chrome';
    }
    else if(!!window.ActiveXObject || "ActiveXObject" in window){
       return 'IE>=11';
    }
    else{
     return 'Unkonwn';
    }
 }

var cook = $.cookie('lock');
if (cook!=undefined&&cook!=""&&cook!=null){}
else{window.location.href="502.html"}
