//���ڶ�ʱ����һ��Ҫ�򿪺�ǵ����
//������ӵ����ʼ��ť�ͻ��һ����ʱ��
//���������˵�����ο�ʼ�󣬴���ʱ����������⣬����ÿ���һ�ξʹ�һ���µĶ�ʱ�������ص���ֻ�����µ�
var s;    //ȫ�ֶ�ʱ��
//�����
function foo() {
    var i1 = document.getElementById("i1");
    var now = new Date();
    i1.value = now.toLocaleTimeString(); //����i1�����������Ϊ��ǰʱ��
}
//��ʼ��ť
var b1 = document.getElementById("b1");
b1.onclick = function() {
    foo();                       //���b1�����ʼ��ť�󣬾͵���foo()����
    if (s === undefined) {     //���ȫ�ֶ�ʱ��Ϊundefined
        s = setInterval(foo,1000);   //������һ��ȫ�ֶ�ʱ��
    }
}
//ֹͣ��ť
var b2 = document.getElementById("b2");
b2.onclick = function() {
    clearInterval(s);           //���ֹͣ����������ʱ����
    console.log(s);     //�����,s��Ȼ��ֵ
    s = undefined;     //���������s����Ϊundefined
}

