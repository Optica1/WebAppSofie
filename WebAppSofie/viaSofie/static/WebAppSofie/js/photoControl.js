function selectPicture(el) {
  var currentTitle = document.getElementById('priorityImage').title;
  $("img[title='"+currentTitle+"']").css({"border": "none"});
  $("#priorityImage").attr("src", el.src);
  $("#priorityImage").attr("title", el.title);
  $("#photolist").find("img[title='"+el.title+"']").css({"border": "thick solid #0d3531"});
}

function imageSelected() {
  var currentTitle = document.getElementById('priorityImage').title;
  $("#photolist").find("img[title='"+currentTitle+"']").css({"border": "thick solid #0d3531"});
}
