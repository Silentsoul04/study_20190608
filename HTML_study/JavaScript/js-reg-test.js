
/*�Ƿ����С��*/
function    isDecimal(strValue )  {
   var  objRegExp= /^\d+\.\d+$/;
   return  objRegExp.test(strValue);
}
;
/*У���Ƿ������������ */
function ischina(str) {
	var reg=/^[\u4E00-\u9FA5]{2,4}$/;   /*������֤���ʽ*/
	return reg.test(str);     /*������֤*/
}

/*У���Ƿ�ȫ��8λ������� */
function isStudentNo(str) {
	var reg=/^[0-9]{8}$/;   /*������֤���ʽ*/
	return reg.test(str);     /*������֤*/
}

/*У��绰���ʽ */
function isTelCode(str) {
	var reg= /^((0\d{2,3}-\d{7,8})|(1[3584]\d{9}))$/;
	return reg.test(str);
}

/*У���ʼ���ַ�Ƿ�Ϸ� */
function IsEmail(str) {
	var reg=/^\w+@[a-zA-Z0-9]{2,10}(?:\.[a-z]{2,4}){1,3}$/;
	return reg.test(str);
}


function  fun1(){
	if(!isStudentNo(document.getElementById("sno").value)){
		alert("ѧ�������8λ����");
		document.getElementById("sno").focus();
		return false;
	}

	if(!ischina(document.getElementById("username").value)){
		alert("ѧ������������д����");
		document.getElementById("username").focus();
		return false;
	}

	if(!IsEmail(document.getElementById("email").value)){
		alert("�����ַ����");
		document.getElementById("email").focus();
		return false;
	}

	if(!isTelCode(document.getElementById("tel").value)){
		alert("�绰���벻��");
		document.getElementById("tel").focus();
		return false;
	}

	/*���е�����˵����֤ͨ������true    submit�ύ��ť�������ύ��*/
	alert("�ύ�ɹ�");
	return false;   // ������ý�ֹ�ύ��ʵ����Ŀ��Ҫ��Ϊ true
}
