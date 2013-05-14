/**
 * Functor that clears value of given element.
 */
field_cleaner = function(element) {
  this.element = element;
  return function() {
    element.value = "";
  };
}




/*
 * Initialization. Adds button that clears file field.
 */
window.onload = function() {
    element = document.getElementById("id_file");
    clean_button = document.createElement("input");
    clean_button.type="button";
    clean_button.value="Clear";
    clean_button.onclick = field_cleaner(element);
    element.parentNode.insertBefore(clean_button, null);
};

