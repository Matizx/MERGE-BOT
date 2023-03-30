import os


class Config(object):
    API_HASH = "409da5b68ad699091fa72b381921f0e5"
    BOT_TOKEN = "6285202665:AAFRmXc-l2wP_04NtlAkfau0_iDZWIZvKBE"
    TELEGRAM_API = 15236804
    OWNER = "1963114305"
    OWNER_USERNAME = "Md_Matin_Ashraf"
    PASSWORD = "ThanksMatin"
    DATABASE_URL = "mongodb+srv://MdMatin:x7bdggKJ9zb9JSK@cluster0.89bzvjn.mongodb.net/?retryWrites=true&w=majority"
    LOGCHANNEL = "-1001812984233"  # Add channel id as -100 + Actual ID
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID","root")
    USER_SESSION_STRING = "BQDofsQAKPLt_WZTCrrd_JvIT9qrTS1DX7_br6z_kA-QFUlnPQG0jXEQ978NUCL33oUr7mbbCc9X2fuTwKhiYH2VsRd5MhFAiRjehix1G0sl8N27vtvzN4f4_uQRsqgwsc0eIRSelh8-CVI1e4_Z0suEPQJUfPdPmH3ZIe0GqDQR0S_hI_ooipZkIkUHlMZdcZTc4Ov1XAuIThidFoiW_bUuoeBFs6FQDpTtW1blqEVEmmqoMkkbHM6WC2KhB5i41tl6C3HdCN3AVuAnFSt4KpTTLqP19m8lZayDrF-K7Kwh_vNYroP9Xrbi9FZCpM7lxUcQui3AjxZuz7RMZvnr9l-oAFCy_AAAAAB1Ar9BAA"
    IS_PREMIUM = "True"
    MODES = ["video-video", "video-audio", "video-subtitle","extract-streams"]
