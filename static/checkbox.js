function checkAll(fldSetID, checktoggle)
{
  var checkboxes = new Array();
  var fldSet = document.getElementById(fldSetID);
  var checkboxes = fldSet.getElementsByTagName('input');

  for (var i=0; i<checkboxes.length; i++)  {
    if (checkboxes[i].type == 'checkbox')   {
      checkboxes[i].checked = checktoggle;
    }
  }
}