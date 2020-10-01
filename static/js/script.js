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
        partner_ip: null,
        connected: null,
        new_user: null,
        status: "Searching stranger...",
        message: "",
        chat_messages:[],
        three_dot_menu:false,
        yesNoModal:{
            title: "Do you want to report stranger?",
            show: false,
            para:[],
            method: null
        }
    },
    updated() {
        chat_message:this.scrollToBottom();
    },
    mounted() {
        console.log("Vue2 mounted");
        this.currentpage = 'Home';
        this.connected = true;
        document.addEventListener('keydown', this.universalEvents.bind(this));
        this.configureSocket();
    },
    methods: {
        // page change functions
        changePage(page){
            switch (page) {
                case "Home":
                    this.currentpage = page;
                    break;
                case "Chat":
                    this.new_user = "Stop";
                    this.currentpage = page;
                    this.searchUser();
                    break;
            }
        },
        // Socket functions
        configureSocket(){
            this.socket.io.autoConnect = false;
            this.socket.io._reconnectionAttempts = 0;
            self = this;
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
                self.partner = data.sid;
                self.partner_ip = data.ip;
                self.chat_messages = [];
                self.new_user = "Stop";
            });

            this.socket.on('disconnect', function(){
                self.partner = null;
                clearTimeout(self.partner_timeout);
                self.connected = false;
                self.status = "Server disconnected. Try reloading the page!";
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
            if(this.connected){
                this.partner = null;
                clearTimeout(this.partner_timeout);
                this.status = "Searching stranger...";
                this.socket.emit('partner');
                this.partner_timeout = setTimeout(()=>{ this.status = "TTS could not find stranger for you. Try again later."; this.socket.emit('stop_search'); this.new_user = "New"; }, 10000);
            }
        },
        sendmsg(){
            if( this.partner != null && this.connected){
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
            if (this.connected){
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

// Popups and menus
        handle2buttonPopup(){
            switch(this.yesNoModal.method){
                case 0 :
                    this.reportStranger();
                    break;
            }
        },
        reset2btnModal(){
            this.yesNoModal={
                title: "Do you want to report stranger?",
                show: false,
                para:[],
                method: null
            }
        },
        showDotMenu(){
            if(this.partner_ip){
                if(!this.three_dot_menu)
                    document.getElementsByClassName("dot-menu")[0].style.visibility = 'visible';
                else
                    document.getElementsByClassName("dot-menu")[0].style.visibility = 'hidden';
                this.three_dot_menu = !this.three_dot_menu;
            }
        },

// Other functions
        scrollToBottom() {
            try{
                let element = (document.getElementById("panelbody"));
                element.scrollTop = element.scrollHeight;
            }
            catch(err){}
        },
        confirmReport(){
            this.showDotMenu();
            this.yesNoModal.title = "Do you want to report stranger?";
            this.yesNoModal.method = 0;
            this.yesNoModal.show = true
        },
        reportStranger(){
            url = "/api/report";
            data = JSON.stringify({
                Stranger_ip: this.Stranger_ip
            });
            response =  apiCall(url, "POST", data);
            response.then(() =>{
                console.log(response);
            })
        },
    },
    beforeDestroy() {
        this.socket.disconnect();
        this.socket.close();
    },
});