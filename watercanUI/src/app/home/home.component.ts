import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service';
import { Globals } from '../globals';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
  searchFlag: boolean = false;

  constructor(private api: ApiService, private global: Globals) {
    console.log('In constructor home...');
    console.log('hello');
  }


  ngOnInit() {
    this.global.searchKey = !this.global.searchKey;
  }

}
