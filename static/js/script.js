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
        this.currentpage = 'Chat';
        this.ConfigureSocket();
        this.connect();
        this.search_user();
    },
    watch: {
        currentpage: function(o,n){
            if(n == 'chat'){
                console.log("Chat");
            }
        }
    },
    methods: {
        // Actual inuse functions
        // page change functions
        // first page home
        changepage(page){
            if (page == "Home")
                this.currentpage = page;
            else if (page == "Chat")
                this.currentpage = page;
        },

        // Socket functions
        ConfigureSocket(){
            this.socket.io.autoConnect = false;
            this.socket.io._reconnectionAttempts = 0;
            self = this
            this.socket.on('message', function(data) {
                self.chat_messages.push(data);
            });
            this.socket.on('online',function(data){
                self.onLine = data;
            })
        },
        connect(){
            self = this
            // this.socket.on('connection', function() {
            //     // self.socket.emit("connected");
            //     console.log("Connected")
            // });
            this.socket.on('disconnect', function(){
                self.partner = null;      
            });
        },
        search_user(){
            if(this.partner == null){
                self = this;
                this.socket.on("partner", function(data){
                    self.partner = data.user;
                });
            }
        },
        sendmsg(){
            if( this.partner != null){
                if (this.message)
                    json = {
                            "message":this.message, 
                            "to": this.partner,
                        }
                    this.socket.send(json);
                    console.log(this.message);
                    // this.socket.emit(json, room=this.partner);
                    this.chat_messages.push(json);
                    this.message = "";
            }
        },

        // extra functions
        scrollToBottom() {
            let element = document.getElementsByClassName("messageBox")[0];
            console.log(element);
            // element.scrollIntoView(true,{behavior: "smooth", block: "end"});
            console.log(element.scrollHeight);
            element.scrollTop = element.scrollHeight;
        }
    },
});