// Grab elements, create settings, etc.
var video = document.getElementById('video');

// Get access to the camera!
if(navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {

// Not adding `{ audio: true }` since we only want video now
navigator.mediaDevices.getUserMedia({ video: true }).then(function(stream) {
  video.src = window.URL.createObjectURL(stream);
  video.play();
  });
}

// Elements for taking the snapshot
var canvas = document.getElementById('canvas');
var context = canvas.getContext('2d');
var video = document.getElementById('video');
var avatarImg;

// Converts canvas to an image
function convertCanvasToImage(can) {
  var image = new Image();
  image = can.toDataURL("image/png");
  return image;
}

// Trigger photo take
document.getElementById("snap").addEventListener("click", function() {
  context.drawImage(video, 0, 0, 640, 480);
  avatarImg = convertCanvasToImage(canvas);
  var blob = base64ToBlob(avatarImg.replace('data:image/png;base64,', ''), 'image/png');
  var formData = new FormData();
  formData.append('avatar', blob);

  $.ajax({
      url: 'api/upload',
      type: "POST",
      cache: false,
      contentType: false,
      processData: false,
      data: formData})
          .done(function(e){
              alert('done!');
          });
  });

function base64ToBlob(base64, mime)
{
    mime = mime || '';
    var sliceSize = 1024;
    var byteChars = window.atob(base64);
    var byteArrays = [];

    for (var offset = 0, len = byteChars.length; offset < len; offset += sliceSize) {
        var slice = byteChars.slice(offset, offset + sliceSize);

        var byteNumbers = new Array(slice.length);
        for (var i = 0; i < slice.length; i++) {
            byteNumbers[i] = slice.charCodeAt(i);
        }

        var byteArray = new Uint8Array(byteNumbers);

        byteArrays.push(byteArray);
    }

    return new Blob(byteArrays, {type: mime});
}
