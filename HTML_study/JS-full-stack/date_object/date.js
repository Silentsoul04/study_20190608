var d1 = new Date();
console.log(d1);
console.log(d1.toLocaleTimeString());
console.log(d1.getDate());
console.log(d1.getDay());

var s = '{"name":"xiaozhan","age":20}';     //this is a json string, �����key���˫���ţ����򱨴�
var ret = JSON.parse(s);    //change json string to js object
console.log(typeof s);
console.log(ret);
console.log('the type of ret:',typeof ret);
var s1 = JSON.stringify(ret);    //change js object to string
console.log(s1);
console.log('the type of s1:',typeof s1);

//RegExp����
// var pattern = /^([A-Za-z0-9_.-])+@([A-Za-z0-9_.-])+.([A-Za-z]{2,4})$/;             //ƥ��󲿷ֵ������ʽ
var pattern = new RegExp("^([A-Za-z0-9_.-])+\@([A-Za-z0-9_.-])+.([A-Za-z]{2,4})$"); //ƥ��󲿷������ʽ

var mail_group= new Array("cn42du@163.com","ifat3@sina.com.cn","ifat3.it@163.com","ifat3_-.@42du.cn");
for (let i=0;i<mail_group.length;i++) {
    ret = pattern.test(mail_group[i]);
    console.log(ret);
    // console.log(mail_group[i]);
}

var reg = new RegExp("^[a-zA-Z0-9_.-]+$");
var s = "xiaozhan_-.";
var ret = reg.test(s);
console.log(ret);

// ����ɾ����Ԫ��
var d1 = document.getElementById("d1");
var d2 = d1.firstElementChild;
// d1.removeChild(d2);  //����ɾ����һ����Ԫ��

//replaceChild
var d1 = document.getElementById("d1");
var d2 = d1.firstElementChild;
var newTag = document.createElement("a");
newTag.innerText = "this is a new link";
newTag.href = "http://www.sogo.com/";
d1.replaceChild(newTag,d2);      //��newTag�滻d2��ǩ
newTag.style.backgroundColor = "yellow";

//class operation
var class_list = document.getElementsByTagName("div");
var class_names = class_list[1].classList;
// class_names.contains("c2");
// class_names.add("c4");
class_names.toggle("c4");    //if exists, remove it otherwise add this class
class_names.remove("c2");


