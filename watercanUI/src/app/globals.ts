import { Injectable } from '@angular/core';

@Injectable()
export class Globals {
  searchFlag: boolean = false;
  searchKey: any;
  itemCount = 0;
  specificItemCount = []
  dict = {}
  summation = 0
}
