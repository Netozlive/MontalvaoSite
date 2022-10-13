function setResize{{ imovei.idd }}() {
  element = document.querySelector('#ratinho');
  element.classList.remove('guri');
  element.classList.add('rapaiz');

  afe = document.querySelector('#ratinhoo');
  afe.classList.remove('coluna-77');
  afe.classList.add('coluna-37');
  
  
  eleg = document.querySelector('#aiframe_c');

  eleg.classList.remove('eia');
  
  eleg.classList.add('calma');

  eleg.src = "{% url 'imoveis:compararimovel' imovei.pk %}";


  afreme = document.querySelector('#aiframe_b');
  afreme.src = "{% url 'imoveis:comparar_tabela' imovei.pk %}";

  afreme.classList.remove('eia');
  
  afreme.classList.add('coluna-37');

  var $wrapper = document.querySelector('.wrapper'),
  // String de texto
  HTMLNovo = "<iframe src='https://www.youtube.com/embed/ag5vVjh0vzQ'></iframe>"+ 
  "<p><h1>A</h1></p>";

// Insere o texto antes do conteúdo atual do elemento
$wrapper.insertAdjacentHTML('afterbegin', HTMLNovo);


}
