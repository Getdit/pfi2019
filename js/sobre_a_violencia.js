$("#botao1").click(function(event){
	$("#botao1").addClass("selecionado");
	$("#botao2").removeClass("selecionado");

	$("#conteudo1").show();
	$("#conteudo2").hide();

});

$("#botao2").click(function(event){
	$("#botao2").addClass("selecionado");
	$("#botao1").removeClass("selecionado");

	$("#conteudo2").show();
	$("#conteudo1").hide();
});

$(function(){
	$("#conteudo2").hide();
});