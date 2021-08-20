function click(){
    var value = document.getElementById("search_equity").value
    if (value ==null || value == undefined || value ==""){
        alert("请输入股票代码");
    }
    else{
        window.location.href="search.php?search="+value;
    }
}

function getKey(event) {
    if (event.keyCode == 13) {
        click()
    }
}

document.getElementById("hand").onclick = function () {
    click()
};