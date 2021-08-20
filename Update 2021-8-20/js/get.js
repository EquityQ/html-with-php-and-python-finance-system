var getParam = function () {
    try{
    var url = window.location.href;
    var result = url.split("?")[1];
    var keyValue = result.split("&");
    var obj = {};
    for (var i = 0; i < keyValue.length; i++) {
        var item = keyValue[i].split("=");
        obj[item[0]] = item[1];
    }
    return item[0]+':'+item[1];}catch(e){
        console.warn("There has no param value!");
    }
};
window.onload = function () {
    console.log(getParam());
}