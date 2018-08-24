/**
 * Created by Administrator on 2018/8/16.
 */
function getXhr() {
  if (window.XMLHttpRequest) {
    return new XMLHttpRequest
  } else {
    return new ActiveXObject('Microsoft.XMLHTTP');
  }
}
