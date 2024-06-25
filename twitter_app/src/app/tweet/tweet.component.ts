import { Component, Input} from '@angular/core';
import { FormsModule } from '@angular/forms';
import { Tweet } from '../interfaces/tweet';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-tweet',
  standalone: true,
  imports: [FormsModule, CommonModule],
  templateUrl: './tweet.component.html',
  styleUrl: './tweet.component.css'
})
export class TweetComponent {
  @Input() tweet!: Tweet;
}
