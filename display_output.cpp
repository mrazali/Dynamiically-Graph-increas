int x = 0;
			InitializeComponent();
			//
			//TODO: Add the constructor code here
			//
			fstream file;
			string comt;
			file.open("post.txt");
			while(!file.eof())
			{
				getline(file,comt);
				//cout<<comt<<endl;
				posts(comt,x);
				x+=40;
				
			}
			file.close();
			
			
			
			
			public: void posts(string p, int x)
		{
			
			String^ str3 = gcnew String(p.c_str());
			Label^ l = gcnew Label;
			l->AutoSize = true;
			l->Size = System::Drawing::Size(355, 42);
			l->Location = System::Drawing::Point(29, 209+x);
			l->Text = str3;


			this->Controls->Add(l);

		}

