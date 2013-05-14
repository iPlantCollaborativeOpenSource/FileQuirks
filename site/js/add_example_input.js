

field_cleaner2 = function(element) {
  this.element = element;
  return function() {
    element.value = ">example fasta\nUUUUUUUUUUU";
  };
}

/*
 * Initialization. Adds button that clears file field.
 */
window.onload = function() {

    element2 = document.getElementById("id_paste");
    clean_button2 = document.createElement("input");
    clean_button2.type="button";
    clean_button2.value="Load sample data";
    clean_button2.onclick = field_cleaner2(element2);
    element2.parentNode.insertBefore(clean_button2, null);
};

