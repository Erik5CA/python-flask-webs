btns = document.querySelectorAll(".btn-delete");
if (btns) {
  const btnArray = Array.from(btns);
  btnArray.forEach((btn) => {
    btn.addEventListener("click", (e) => {
      if (!confirm("Are you sure you want delete it?")) {
        e.preventDefault();
      }
    });
  });
}
