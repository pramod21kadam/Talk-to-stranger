var app = new Vue({
    el: "#app",
    delimiters: ["<%","%>"],
    data: {
        currentpage: null,
        onLine: 0,
        socket: io(),
        typing: null,
        typing_timeout:null,
        partner_timeout: null,
        partner: null,
        new_user: null,
        status: "Searching stranger...",
        message: "",
        chat_messages:[]
    },
    updated() {
        chat_message:this.scrollToBottom();
    },
    mounted() {
        console.log("Vue2 mounted");
        this.currentpage = 'Home';
        document.addEventListener('keydown', this.universalEvents.bind(this));
        this.configureSocket();
    },
    methods: {
        // page change functions
        changePage(page){
            if (page == "Home"){
                this.currentpage = page;
                return;
            }
            if (page == "Chat"){
                this.new_user = "Stop";
                this.currentpage = page;
                this.searchUser();
                return;
            }
        },
        // Socket functions
        configureSocket(){
            this.socket.io.autoConnect = false;
            this.socket.io._reconnectionAttempts = 0;
            self = this;
            // this.socket.on('connection', function() {
            //     console.log("Connected to server");
            // });
            this.socket.on('message', function(data) {
                if (data['from'] == self.partner){
                    clearTimeout(self.typing_timeout);
                    data['from'] = "stranger";
                    self.typing = "";
                    self.chat_messages.push(data);
                }
            });
            this.socket.on('online',function(data){
                self.onLine = data;
            });

            this.socket.on("partner", function(data){
                clearTimeout(self.partner_timeout);
                self.status = "You are talking to random stranger. Happy chatting! 😊";
                self.partner = data;
                self.chat_messages = [];
                self.new_user = "Stop";
            });

            this.socket.on('disconnect', function(){
                self.partner = null;
                self.status = "Server disconnected. Try again!";
                console.log("Server Disconnected");      
            });
            this.socket.on('typing', function(){
                clearTimeout(self.typing_timeout);
                self.typing = "Stranger is typing...";
                self.typing_timeout = setTimeout(()=>{self.typing = "";}, 2000);
            });
            
            this.socket.on('leave_room',function(){
                self.status = "Stranger left the room. Press on new button to start search.";
                self.partner = null;
                self.new_user = "New";
            });

            this.socket.on('keys',function(data){
                console.log(data);
            });
        },

// Socket functions
        searchUser(){
            this.partner = null;
            clearTimeout(this.partner_timeout);
            this.status = "Searching stranger...";
            this.socket.emit('partner');
            this.partner_timeout = setTimeout(()=>{ this.status = "TTS could not find stranger for you. Try again later."; this.socket.emit('stop_search'); this.new_user = "New"; }, 10000);
        },
        sendmsg(){
            if( this.partner != null){
                if (this.message){
                    json = {
                            "message":this.message, 
                            "to": this.partner,
                            "from": this.socket.io.engine.id
                        }
                    this.socket.emit('message',json);
                    json['from'] = "self";
                    self.new_user = "Stop";
                    this.chat_messages.push(json);
                    this.message = "";
                    }
            }
        },
        changeUserStatus(){
            if(this.new_user == "Stop"){
                this.new_user = "Sure?";
            }
            else{ 
                if(this.new_user == "Sure?"){
                    this.status = "You left the chat";
                    this.socket.emit('leave_room',{"partner": this.partner});
                    this.new_user = "New";
                    this.partner = null;
                } 
                else if(this.new_user == "New"){
                    this.new_user = "Searching..";
                    this.searchUser();
                }
            }
        },


//  Event functions
        inputBoxEvents(event){
            switch(event.key){
                case "Enter":
                    this.sendmsg();
                    break;
                default:
                    this.socket.emit("typing", {"partner": this.partner});
                    break;
            }
        },
        universalEvents(events){
            switch(event.key){
                case "Escape":
                    this.changeUserStatus();
                    break;
            }
        },

// extra functions
        scrollToBottom() {
            try{
                let element = (document.getElementById("panelbody"));
                element.scrollTop = element.scrollHeight;
            }
            catch(err){}
        },
    },
    beforeDestroy() {
        this.socket.disconnect();
        this.socket.close();
        console.log('Main Vue destroyed');
    },
});