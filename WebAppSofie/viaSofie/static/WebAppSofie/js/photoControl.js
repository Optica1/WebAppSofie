function selectPicture(el) {
  var currentTitle = document.getElementById('priorityImage').title;
  $("img[title='"+currentTitle+"']").css({"border": "none"});
  $("#priorityImage").attr("src", el.src);
  $("#priorityImage").attr("title", el.title);
  imageSelected();
}

function imageSelected() {
  $("#photolist").find('img').each(function() {
    var priorityImage = document.getElementById('priorityImage');
    if (this.title == priorityImage.title){
      this.style.border = "thick solid #0d3531";
      return;
    }
  });
}

function unselectImage() {
  $("#photolist").find('img').each(function() {
    var priorityImage = document.getElementById('priorityImage');
    if (this.title == priorityImage.title){
      this.style.border = "thick solid #0d3531";
      return;
    }
  });
}
