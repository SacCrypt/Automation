gPt = function (c) {
  if (c.id !== "") {
    return 'id("' + c.id + '")';
  }
  if (c === document.body) {
    return c.tagName;
  }
  var a = 0;
  var e = c.parentNode.childNodes;
  for (var b = 0; b < e.length; b++) {
    var d = e[b];
    if (d === c) {
      return gPt(c.parentNode) + "/" + c.tagName + "[" + (a + 1) + "]";
    }
    if (d.nodeType === 1 && d.tagName === c.tagName) {
      a++;
    }
  }
};
return gPt(arguments[0]).toLowerCase();
