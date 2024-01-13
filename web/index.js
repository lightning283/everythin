eel.expose(set_loading_cursor);
eel.expose(reset_cursor);

function set_loading_cursor() {
    document.body.style.cursor = 'wait';
}

function reset_cursor() {
    document.body.style.cursor = 'default';
}
document.getElementById("download-btn").addEventListener("click" , async() => {
    let link = document.getElementById("download-input").value
    await eel.download_video(link)(function(url) {
        var videoElement = document.createElement("video");
        videoElement.width = 640;
        videoElement.height = 360;
        videoElement.controls = true;
        videoElement.autoplay = true;
        var sourceElement = document.createElement("source");
        sourceElement.src = url; 
        sourceElement.type = "video/mp4";
        videoElement.appendChild(sourceElement);
        document.getElementById("videoContainer").appendChild(videoElement);
    });
})