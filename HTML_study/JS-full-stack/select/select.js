 let data = {1:["chaoyang","haidian","shunyi"], 2:["pudong","yangpu","xuhui"]};  //js�е�object���������ֵ�
 let s1 = document.getElementById("s1");
 s1.onchange = function() {
     console.log(this .value);      //ȡ����һ����
     var areas = data[this.value];   //ȡ����Ӧ�е���
     var s2 = document.getElementById("s2"); //�ҵ���Ӧ����
     s2.innerText = "";    //���֮ǰ������
     for(let i=0;i<areas.length;i++) {
         var optEle = document.createElement("option");  //������ǩoption
         optEle.innerText = areas[i]; //����ǩ��ֵ
         s2.appendChild(optEle);      //��ӱ�ǩ��ĳ��λ��
     }
 }