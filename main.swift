import Foundation
import Crypto


func makehash(string: String) -> String {
    guard let stringData = string.data(using: .utf8) else {
        fatalError("FAiled to obtain data from String.")
    }                

    let hash = Insecure.MD5.hash(data: stringData)
    let hashData = Data(hash)

    let hexadecimalHash = hashData.map { String(format: "%02hhx", $0) }.joined()
    return hexadecimalHash
}
let x = makehash(string:"WLDME_FOREVER2005")
print(x)
