from matplotlib import pyplot as plt
#matplotlib library is for graph plotting and and pyplot module provides simple function for visualization

languages=['React','Scala','MATLAB','Python','Java','C++','C']  #Data have been defined
weights=[3,1.2,3.8,4.7,2,1,1.5]

fig,ax=plt.subplots(1,2, figsize=(12,5))
#plt.subplots(1,2): this creates two side by side plots in one row 2 columns
#figsize=(12,5) sets the figure size with width 12 and height 5
fig.canvas.manager.set_window_title('15139531_Shangeeth_Visualization')
ax[0].pie(weights,labels=languages, autopct='%1.2f%%', shadow=True, explode=(0,0,0,0.15,0,0,0))
ax[0].set_title('Programming Languages Popularity')
#Here pie create the pie chart and labels will set names on it and autopct will give percentage according to their weights in two decimal places
#Shadow will add shadow effect and explode will seperate python from pie chard like explode effect
#set title will give name for piechart

ax[1].bar(languages,weights,color='skyblue',edgecolor='black')
ax[1].set_xlabel('Programming Languages')
ax[1].set_ylabel('Popularity weight')
ax[1].set_title('Bar Chart of Programming languages')
#bar create barchart with bar color skyblue and bar edge in black color
#name the x axis and y axis as provided names respectively
#followingly the set title provide a title for bar chart

plt.tight_layout()  #This will prevent from overlapping by giving spaces
plt.show()  #Display final figure. WOW-1