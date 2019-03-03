var Slide_list = [
    { pdf_name: 'W1_Regression', pageNumber: 39},
    { pdf_name: 'W1_Bias_and_Variance', pageNumber: 22},
    { pdf_name: 'W2_Classification', pageNumber: 35},
    { pdf_name: 'W2_Gradient Descent', pageNumber: 39},
    { pdf_name: 'W2_Logistic Regression', pageNumber: 38}
    // { pdf_name: '', pageNumber: }
];

// Initial 
window.onload = function () {
	// alert("It's loaded!") 
	var slideSelect=document.getElementById("slide-list");
	var inner = "";
	for(var i = 0; i < Slide_list.length; i++){
	    inner = inner+'<option value=i>' + Slide_list[i].pdf_name + '</option>';
	}
	slideSelect.innerHTML=inner;
	setPdfOnScreen(0)
}

function setPdfOnScreen(index) {
	document.getElementById('display').innerHTML = '';
	var target = Slide_list[index]
	for (var i = 0; i < Slide_list[index].pageNumber; i++) {
		document.getElementById('display').innerHTML += '<p style="font-size:10px;">'+
			'![0](./JPG/' + target.pdf_name+'/'+target.pdf_name+'_'+ i +'.jpg) </p>'+
			'<img src="./JPG/' + target.pdf_name + '/'+target.pdf_name+'_'+ i +'.jpg" '+
				'alt="Oops GG" width="100%" height="100%" onclick="copyText(this.src)"><br>'
	}
}

function changeSlide(index) {
	// alert("Test!") 
	setPdfOnScreen(index)
}

function copyText(src) {
	var tmpStr = "./JPG/"+src.split("JPG")[1]
	// alert("Test! "+tmpStr)
	copyStringToClipboard(tmpStr)
}

// Reference: https://techoverflow.net/2018/03/30/copying-strings-to-the-clipboard-using-pure-javascript/
function copyStringToClipboard (str) {
   // Create new element
   var el = document.createElement('textarea');
   // Set value (string to be copied)
   el.value = str;
   // Set non-editable to avoid focus and move outside of view
   el.setAttribute('readonly', '');
   el.style = {position: 'absolute', left: '-9999px'};
   document.body.appendChild(el);
   // Select text inside element
   el.select();
   // Copy text to clipboard
   document.execCommand('copy');
   // Remove temporary element
   document.body.removeChild(el);
}