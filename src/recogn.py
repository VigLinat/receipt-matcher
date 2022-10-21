from lib import Recognition as recog, \
                ImageProcessor as improc, \
                Receipt

if __name__ == '__main__':

    imagesToProcess = ['okey1-soft-cropp.jpg']
    receiptsBase = 'receipts/'
    resultsBase = 'results/'
    saveas = '';
    for file in imagesToProcess:
        saveas = resultsBase \
            + 'receipt-output-' \
            + file[0 : len(file) - len('.jpg')] \
            + '.txt' # crop the .jpg extension from file name 

        preprocessor = improc.ImageProcessor(receiptsBase+file)
        preprocImage = preprocessor.preprocImage(['grayscale'])
        
        ocr = recog.Recognition(preprocImage)
        text = ocr.doRecognition()

        
        with open(saveas, 'w', encoding= 'utf-8') as output_file:
            output_file.write(text)

    textfile = open(saveas, 'r', encoding= 'utf-8')
    text = textfile.read()
    print(text)
    rmatcher = Receipt.ReceiptMatcher()
    receipt = rmatcher.makeReceipt(text)
    receipt.printReceipt()
