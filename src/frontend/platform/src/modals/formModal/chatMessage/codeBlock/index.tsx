import { Download, Check, Clipboard } from 'lucide-react';
import { useState } from "react";
import { Prism as SyntaxHighlighter } from "react-syntax-highlighter";
import { oneDark } from "react-syntax-highlighter/dist/cjs/styles/prism";
import { copyText, programmingLanguages } from "../../../../utils";

interface Props {
  language: string;
  value: string;
}

export function CodeBlock({ language, value }) {
  const [isCopied, setIsCopied] = useState<Boolean>(false);

  const copyToClipboard = () => {
    setIsCopied(true);
    copyText(value).then(() => {
      setTimeout(() => {
        setIsCopied(false);
      }, 2000);
    })
  };
  const downloadAsFile = () => {
    const fileExtension = programmingLanguages[language] || ".file";
    const suggestedFileName = `${"generated-code"}${fileExtension}`;
    const fileName = window.prompt("enter file name", suggestedFileName);

    if (!fileName) {
      // user pressed cancel on prompt
      return;
    }

    const blob = new Blob([value], { type: "text/plain" });
    const url = URL.createObjectURL(blob);
    const link = document.createElement("a");
    link.download = fileName;
    link.href = url;
    link.style.display = "none";
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    URL.revokeObjectURL(url);
  };
  return (
    <div className="codeblock font-sans text-[16px]">
      <div className="code-block-modal">
        <span className="code-block-modal-span">{language}</span>

        <div className="flex items-center">
          <button className="code-block-modal-button" onClick={copyToClipboard}>
            {isCopied ? <Check size={18} /> : <Clipboard size={18} />}
            {isCopied ? "Copied!" : "Copy code"}
          </button>
          <button className="code-block-modal-button" onClick={downloadAsFile}>
            <Download size={18} />
          </button>
        </div>
      </div>

      <SyntaxHighlighter
        className="overflow-auto"
        language={language}
        style={oneDark}
        customStyle={{ margin: 0 }}
      >
        {value}
      </SyntaxHighlighter>
    </div>
  );
}
CodeBlock.displayName = "CodeBlock";
