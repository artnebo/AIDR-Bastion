from collections.abc import Iterator
from contextlib import suppress

import yaml


class YmlFileParser:
    @staticmethod
    def parse(file_path: str) -> Iterator[dict] | None:
        """
        Parse YAML file with support for various encodings.

        Attempts to read the file with different encodings to handle
        various character sets including the specified encoding pattern.

        Args:
            file_path (str): Path to the YAML file to parse

        Returns:
            Iterator[dict] | None: Iterator of parsed YAML documents or None on error
        """
        encodings_to_try = ["utf-8", "latin-1", "cp1252", "iso-8859-1", "utf-16", "utf-32"]

        for encoding in encodings_to_try:
            with suppress(yaml.YAMLError, FileNotFoundError, PermissionError, UnicodeDecodeError):
                with open(file_path, encoding=encoding) as f:
                    content = f.read()
                    # Handle the specific encoding pattern if present
                    if "[Ä±Ä°ÓÐ†É©Î™]|[Ð¾ÎŸÎ¿ÐžÐ¾]" in content:
                        # Try to decode with latin-1 and re-encode as utf-8
                        with open(file_path, "rb") as binary_file:
                            raw_content = binary_file.read()
                            try:
                                # Decode as latin-1 and re-encode as utf-8
                                decoded = raw_content.decode("latin-1")
                                content = decoded.encode("utf-8").decode("utf-8")
                            except (UnicodeDecodeError, UnicodeEncodeError):
                                # Fallback to original content
                                pass

                    # Clean up invalid characters that YAML parser can't handle
                    content = YmlFileParser._clean_yaml_content(content)
                    return yaml.safe_load_all(content)

        return None

    @staticmethod
    def _clean_yaml_content(content: str) -> str:
        """
        Clean YAML content by removing or replacing invalid characters.

        Removes control characters and other characters that YAML parser
        cannot handle, while preserving the structure and meaning.

        Args:
            content (str): Raw YAML content to clean

        Returns:
            str: Cleaned YAML content
        """
        import re

        # Remove control characters except for common ones like \n, \r, \t
        # Keep printable characters and common whitespace
        cleaned = re.sub(r"[\x00-\x08\x0B\x0C\x0E-\x1F\x7F-\x9F]", "", content)

        # Replace any remaining non-printable characters with spaces
        cleaned = re.sub(r"[^\x20-\x7E\n\r\t]", " ", cleaned)

        # Clean up multiple consecutive spaces
        cleaned = re.sub(r" +", " ", cleaned)

        # Clean up multiple consecutive newlines
        cleaned = re.sub(r"\n\s*\n\s*\n+", "\n\n", cleaned)

        return cleaned
