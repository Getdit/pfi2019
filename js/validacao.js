function enviardados() {
  if (document.comentario.mensagem.value == ""){
    alert("O campo MENSAGEM é obrigatório!");
    document.sugestao.email.focus();
    return false;
  }
  return true;
}