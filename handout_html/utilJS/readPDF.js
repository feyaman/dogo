var Slide_list = [
	{ pdf_name: 'Introduction_of_this_course', pageNumber: 63},
	{ pdf_name: 'Regression', pageNumber: 39},
	{ pdf_name: 'Where_does_the_error_come_from?', pageNumber: 22},
	{ pdf_name: 'Gradient_Descent', pageNumber: 38},
	{ pdf_name: 'Classification-Probabilistic_Generative_Model', pageNumber: 35},
	{ pdf_name: 'Classification-Logistic_Regression', pageNumber: 38},
	{ pdf_name: 'Introduction_of_Deep_Learning', pageNumber: 29},
	{ pdf_name: 'Backpropagation', pageNumber: 18},
	{ pdf_name: 'Hello_world_of_Deep_Learning', pageNumber: 17},
	{ pdf_name: 'Tips_for_Deep_Learning', pageNumber: 52},
	{ pdf_name: 'Convolutional_Neural_Network', pageNumber: 49},
	{ pdf_name: 'Why_Deep', pageNumber: 34},
	{ pdf_name: 'Semi-supervised_Learning', pageNumber: 32},
	{ pdf_name: 'Unsupervised_Learning-Principle_Component_Analysis', pageNumber: 34},
	{ pdf_name: 'Unsupervised_Learning-Neighbor_Embedding', pageNumber: 15},
	{ pdf_name: 'Unsupervised_Learning-Deep_Auto-encoder', pageNumber: 29},
	{ pdf_name: 'Unsupervised_Learning-Word_Embedding', pageNumber: 24},
	{ pdf_name: 'Unsupervised_Learning-Deep_Generative_Model', pageNumber: 70},
	{ pdf_name: 'Transfer_Learning', pageNumber: 40},
	{ pdf_name: 'Recurrent_Neural_Network', pageNumber: 89},
	{ pdf_name: 'Matrix_Factorization', pageNumber: 8},
	{ pdf_name: 'Ensemble', pageNumber: 43},
	{ pdf_name: 'Introduction_of_Structured_Learning', pageNumber: 66},
	{ pdf_name: 'Introduction_of_Reinforcement_Learning', pageNumber: 57}
	// { pdf_name: 'W1_Regression', pageNumber: 39},
	// { pdf_name: 'W1_Bias_and_Variance', pageNumber: 22},
	// { pdf_name: 'W2_Classification', pageNumber: 35},
	// { pdf_name: 'W2_Gradient_Descent', pageNumber: 39},
	// { pdf_name: 'W2_Logistic_Regression', pageNumber: 38}
];

// Initial
window.onload = function () {
	// alert("It's loaded!")
	var slideSelect=document.getElementById("slide-list");
	var inner = "";
	for(var i = 0; i < Slide_list.length; i++){
		inner = inner+'<option value=i>'+ (i+1)+ '. ' + Slide_list[i].pdf_name + '</option>';
	}
	slideSelect.innerHTML=inner;
	setPdfOnScreen(0)
}

function setPdfOnScreen(index) {
	document.getElementById('display').innerHTML = '';
	var target = Slide_list[index]
	for (var i = 0; i < Slide_list[index].pageNumber; i++) {
		document.getElementById('display').innerHTML +=
		// '<p style="font-size:10px;"> ![0](./JPG/' + target.pdf_name+'/'+target.pdf_name+'_'+ i +'.jpg) </p>'+
		'<img src="../JPG/' + target.pdf_name + '/'+target.pdf_name+'_'+ i +'.jpg" '+
			'alt="Oops GG" class="pdfImage" width="100%" height="100%" onclick="copyText(this.src)"><br>'
	}
}

function changeSlide(index) {
	// alert("Test!")
	setPdfOnScreen(index)
}

function copyText(src) {
	var tmpStr = '<img src="http://ai.ntu.edu.tw/aho/JPG'+src.split("JPG")[1]+'" width="70%">'
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