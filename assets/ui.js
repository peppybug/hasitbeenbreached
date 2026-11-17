/* Look and feel only: scroll reveal and the ticker pause button. */
(function () {
  var els = document.querySelectorAll('.rv');
  function showAll() { for (var i = 0; i < els.length; i++) els[i].classList.add('in'); }
  try {
    if (!('IntersectionObserver' in window)) showAll();
    else {
      var io = new IntersectionObserver(function (en) { en.forEach(function (x) { if (x.isIntersecting) { x.target.classList.add('in'); io.unobserve(x.target); } }); }, { threshold: .12 });
      for (var i = 0; i < els.length; i++) io.observe(els[i]);
    }
    var t = document.getElementById('ticker'), b = document.getElementById('pause');
    if (t && b) b.addEventListener('click', function () { var p = t.classList.toggle('paused'); b.textContent = p ? 'Play motion' : 'Pause motion'; b.setAttribute('aria-pressed', p); });
  } catch (e) { showAll(); }
})();
