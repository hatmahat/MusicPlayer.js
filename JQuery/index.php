<html>
<head>
    <style type="text/css">
        #circle {
            width: 150px;
            height: 150px;
            border-radius: 0%;
            background-color: rgb(3, 136, 172);
            margin: 10px;
            color: white;
            font-family: arial;
            text-align: center;
            line-height: 150px;
            font-size: 130px;
        }
        .square {
            width: 150px;
            height: 150px;
            background-color: rgb(115, 29, 122);
            margin: 10px;
        }
        p {
            display: none;
        }
    </style>
    <title>
        JQuery
    </title>
    <script type="text/javascript" src="JQuery2.min.js"></script>
</head>
<body>
    <div id="circle">H</div>
    <script type="text/javascript">
        $("#circle").click(function(){
            if ($("#circle").css("width") == "150px") {
                $(this).animate({
                width:"400px", 
                height:"400px",
                marginLeft:"100px",
                marginTop:"100px",
                lineHeight:"400px",
                fontSize:"330px"
                }, 500, function(){
                    $(this).css("background-color", "rgb(3, 136, 172)");
                });
            } else {
                $(this).animate({
                width:"150px", 
                height:"150px",
                margin:"10px",
                lineHeight:"150px",
                fontSize:"130px"
                }, 500, function(){
                    $(this).css("background-color", "rgb(3, 136, 172)");
                });
            };     
        });
    </script>
</body>
</html>