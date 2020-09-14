var app = new Vue({
    el: "#app",
    delimiters: ["<%","%>"],
    data: {
        currentpage: null,
        onLine: 0,
        showBackOnline: false,
        socket: io(),
        string:"123",
        partner: null,
        message: "",
        chat_messages:[]
    },
    mounted() {
        console.log("Vue2 mounted");
        this.currentpage = 'Home';
        this.ConfigureSocket();
    },
    methods: {
        // Actual inuse functions
        // page change functions
        changepage(page){
            if (page == "Home")
                this.currentpage = page;
            else if (page == "Chat"){
                this.currentpage = page;
                this.search_user();
            console.log("Page changed")
            }
        },
        // Socket functions
        ConfigureSocket(){
            this.socket.io.autoConnect = false;
            this.socket.io._reconnectionAttempts = 0;
            self = this
            this.socket.on('connection', function() {
                console.log("Connected")
            });
            this.socket.on('message', function(data) {
                self.chat_messages.push(data);
                console.log(self.chat_messages);
            });
            this.socket.on('online',function(data){
                self.onLine = data;
                // self.formatOnlineCounter();
            });
            this.socket.on("partner", function(data){
                console.log(data);
                self.partner = data;
            });
            this.socket.on('disconnect', function(){
                self.partner = null;
                console.log("Server Disconnected");      
            });
        },
        search_user(){
            console.log("searching Partner");
            if(this.partner == null){
                self = this;
                console.log("searching Partner");
                this.socket.emit('partner');
                // this.socket.send("partner");
            }
        },
        sendmsg(){
            if( this.partner != null){
                if (this.message){
                    json = {
                            "message":this.message, 
                            "to": this.partner,
                        }
                    this.socket.emit('message',json);
                    console.log(this.message);
                    this.chat_messages.push(json);
                    this.message = "";
                    }
            }
        },

        // extra functions
        scrollToBottom() {
            let element = document.getElementsByClassName("messageBox")[0];
            console.log(element);
            // element.scrollIntoView(true,{behavior: "smooth", block: "end"});
            console.log(element.scrollHeight);
            element.scrollTop = element.scrollHeight;
        },

        formatOnlineCounter(){
            console.log(String(this.onLine).length);
        }
    },
});