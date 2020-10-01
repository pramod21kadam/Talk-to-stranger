function apiCall(apiUrl, methodType, dataBody=null) {
    return fetch(apiUrl, {
            method: methodType,
            body: dataBody,
            // credentials: 'include',
        })
        .then(response => {
            if (response.status == 200) {
                return response.json()
            } else{
                console.log(status);
                return response.status
            }
        })
}