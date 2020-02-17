import { Injectable } from '@angular/core';
import { HttpClient } from  '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ClientService {

  constructor(private  httpClient:  HttpClient) { }

  public getClients(){
    return this.httpClient.get('http://10.12.0.2:8080/clients?format=json')
  }
}
