import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';



@Injectable({
  providedIn: 'root'
})
export class ApiService {

  baseurl = "http://127.0.0.1:8000/api/v1";

  httpHeaders = new HttpHeaders({'Content-Type':'application/json'})

  constructor(private http: HttpClient) { }

  // API invovation example
  getProduct(): Observable<any>{
    return this.http.get(this.baseurl + '/product/', {headers: this.httpHeaders});
  }

  getProductDetails(): Observable<Blob>{
    return this.http.get(this.baseurl + '/product_details/', {headers: this.httpHeaders}, {responseType: "blob"});
  }

}
